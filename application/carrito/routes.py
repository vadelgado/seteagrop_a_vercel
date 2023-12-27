from datetime import datetime
from flask import redirect, render_template, request, session, url_for, current_app
from flask_login import login_required
from flask_wtf.csrf import CSRFProtect
from application import db
from . import carrito
from flask_login import current_user

csrf = CSRFProtect()

fecha_actual = datetime.now()


@carrito.route("/cart")
def cart():
    """Función para mostrar los productos que tiene en el carrito de compras"""
    data = {
        "titulo": " Carrito de compras",
    }
    return render_template("carrito/cart.html", data=data)


@carrito.route("/cart", methods=["POST"])
@login_required
@csrf.exempt
def add_product_to_cart():
    """
    Funcion para agregar productos al carrito
    """
    _quantity = int(request.form["quantity"])
    _code = request.form["code"]
    # Validar los valores recibidos
    try:
        if _quantity and _code and request.method == "POST":
            with db.connection.cursor() as cur:
                cur.execute("SELECT * FROM producto WHERE code = %s", (_code,))
                row = cur.fetchone()
                if row:
                    row = {desc[0]: value for desc, value in zip(cur.description, row)}
                    itemArray = {
                        row["code"]: {
                            "name": row["name"],
                            "code": row["code"],
                            "description": row["description"],
                            "quantity": float(_quantity),
                            "price": float(row["price"]),
                            "image": row["image"],
                            "total_price": float(_quantity) * float(row["price"]),
                        }
                    }

                    all_total_price = 0
                    all_total_quantity = 0

                    session.modified = True
                    if "cart_item" in session:
                        if row["code"] in session["cart_item"]:
                            for key, value in session["cart_item"].items():
                                if row["code"] == key:
                                    old_quantity = session["cart_item"][key]["quantity"]
                                    total_quantity = old_quantity + _quantity
                                    session["cart_item"][key][
                                        "quantity"
                                    ] = total_quantity
                                    session["cart_item"][key]["total_price"] = (
                                        total_quantity * row["price"]
                                    )
                        else:
                            session["cart_item"].update(itemArray)
                    else:
                        session["cart_item"] = itemArray

                    for key, value in session["cart_item"].items():
                        individual_quantity = int(value["quantity"])
                        individual_price = float(value["total_price"])
                        all_total_quantity += individual_quantity
                        all_total_price += individual_price
                else:
                    return "Producto no encontrado en la base de datos"

                session["all_total_quantity"] = all_total_quantity
                session["all_total_price"] = all_total_price
                next_page = request.form.get("next")
                if next_page is None:
                    next_page = url_for("carrito.cart")
                return redirect(next_page)
                # return redirect(url_for('bienvenida.index'))
        else:
            return "Error al agregar productos al carrito"
    except ImportError as ex:
        current_app.logger.error(
            f"{fecha_actual} Error al agregar productos al carrito {ex}"
        )


@carrito.route("/empty_cart")
def empty_cart():
    """Funcion para quitar los productos del carrito"""
    try:
        session.pop("cart_item", None)
        session.pop("all_total_quantity", None)
        session.pop("all_total_price", None)
        return redirect(url_for("carrito.cart"))
    except Exception as e:
        current_app.logger.error(f"{fecha_actual} Error al vaciar el carrito {e}")


@carrito.route("/delete/<string:code>")
def delete_product(code):
    """Funcio para eliminar productos especificos del carrito"""
    try:
        all_total_price = 0
        all_total_quantity = 0
        session.modified = True

        for item in session["cart_item"].items():
            if item[0] == code:
                session["cart_item"].pop(item[0], None)
                if "cart_item" in session:
                    for key, value in session["cart_item"].items():
                        individual_quantity = int(session["cart_item"][key]["quantity"])
                        individual_price = float(
                            session["cart_item"][key]["total_price"]
                        )
                        all_total_quantity = all_total_quantity + individual_quantity
                        all_total_price = all_total_price + individual_price
                break

        if all_total_quantity == 0:
            session.pop("cart_item", None)
            session.pop("all_total_quantity", None)
            session.pop("all_total_price", None)
        else:
            session["all_total_quantity"] = all_total_quantity
            session["all_total_price"] = all_total_price
        return redirect(url_for("carrito.cart"))
    except ImportError as e:
        current_app.logger.error(
            f"{fecha_actual} Error al eliminar productos al carrito {e}"
        )


@carrito.route("/update_quantity/<string:code>", methods=["POST"])
@login_required
@csrf.exempt
def update_quantity(code):
    try:
        new_quantity = float(request.form["new_quantity"])

        if "cart_item" in session and code in session["cart_item"]:
            # Convert the price to a float before performing the operation
            price = float(session["cart_item"][code]["price"])

            session["cart_item"][code]["quantity"] = new_quantity
            session["cart_item"][code]["total_price"] = new_quantity * float(price)

            # Update the overall total
            all_total_quantity = sum(
                float(item["quantity"]) for item in session["cart_item"].values()
            )
            all_total_price = sum(
                item["total_price"] for item in session["cart_item"].values()
            )

            session["all_total_quantity"] = all_total_quantity
            session["all_total_price"] = all_total_price

            return redirect(url_for("carrito.cart"))
    except Exception as e:
        current_app.logger.error(
            f"{fecha_actual} Error al actualizar la cantidad del producto {code}: {e}"
        )
        return redirect(url_for("carrito.cart"))


@carrito.route("/checkout", methods=["GET", "POST"])
@login_required
@csrf.exempt
def checkout():
    cart_items = session.get("cart_item", {})
    total_quantity = session.get("all_total_quantity", 0)
    total_price = session.get("all_total_price", 0)

    if request.method == "POST":
        # Perform the checkout process here (e.g., update database, create order, etc.)
        # After successful checkout, clear the cart
        session.pop("cart_item", None)
        session.pop("all_total_quantity", None)
        session.pop("all_total_price", None)
        return redirect(url_for("carrito.cart"))
    
    # If it's a GET request, render the checkout page
    data = {
        "titulo": "Verificar Compra",
        "cart_items": cart_items,
        "total_quantity": total_quantity,
        "total_price": total_price,
    }
    return render_template("carrito/checkout.html", data=data)