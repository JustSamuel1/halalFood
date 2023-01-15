
let slugs_quantity_input = document.getElementById('slugs_quantity');
slugs_quantity_input.value = ''


if (localStorage.getItem('userCart') != null) {
    console.log('Batiscaf 1');
    cart = new Map(JSON.parse(localStorage.userCart));

    var slugs_quantity_var = '';

    cart.forEach((value, key, map) => {
        slugs_quantity_var += String(value);
        slugs_quantity_var += key;
        slugs_quantity_var += '.';
    });

    console.log(localStorage.getItem('userCart').length);
    slugs_quantity_input.value = slugs_quantity_var.slice(0, -1);
    }
    else{
    console.log('Batiscaf 2');
    let cart_form = document.getElementById('form_container_id');
    cart_form.style.display = 'none';
    }

