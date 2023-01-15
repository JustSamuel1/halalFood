
var Cart = new Map();

if (localStorage.getItem('userCart')!=null){
    Cart = new Map(JSON.parse(localStorage.userCart));

    Cart.forEach((value, key, map) => {
        change_quantity(key, value);
    });
}

document.onclick = event => {
    if(event.target.id == 'plus_qnt'){
        let ID = event.target.dataset.id;
        console.log(ID);

        if(Cart.has(ID)){
            let quantity = Cart.get(ID);
            Cart.set(ID, ++quantity);
            change_quantity(ID, quantity);
            console.log("Product quantity: ", Cart.get(ID));
        }
        else{
            Cart.set(ID, 1);
            change_quantity(ID, 1);
            console.log("Product quantity: ", Cart.get(ID));
        }
        localStorage.userCart = JSON.stringify(Array.from(Cart.entries()));
    }

    if(event.target.id == 'minus_qnt'){
        let ID = event.target.dataset.id;
        console.log(ID);

        if(Cart.has(ID)){
            let quantity = Cart.get(ID);
            Cart.set(ID, --quantity);
            change_quantity(ID, quantity);
            if(quantity == 0){
                Cart.delete(ID);
                console.log("Product has been deleted");
            }

            console.log("Product quantity: ", Cart.get(ID));
        }
        localStorage.userCart = JSON.stringify(Array.from(Cart.entries()));
    }
}


function change_quantity(product_id, quantity)
{
    let span_quantity = document.getElementById(product_id);
    span_quantity.innerHTML = String(quantity);
    console.log("Im trying to change it ${quantity} ")

}

