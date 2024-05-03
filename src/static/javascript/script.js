searchBarInput = document.querySelector('.search_bar input')
searchBarInput.addEventListener('click',(e)=>{
    e.preventDefault()
})

const s=document.querySelectorAll("input[type=radio]")
document.addEventListener('click', function(e){
    if (e.target.className=='custom-radio'){
        console.log(e.target)
        let l=e.target.parentElement.getAttribute('href')
        window.open(l, "_top")
    }
    else if (e.target.className=='custom-radio-cirlce'){
        console.log(e.target)
        let l=e.target.parentElement.getAttribute('href')
        window.open(l, "_top")
    }
})



let compteurs = document.querySelectorAll('.compteur');
const plusBtns = document.querySelectorAll(".compteur .bi-plus");
const minusBtns = document.querySelectorAll(".compteur .bi-dash");
// const inputCompteur = document.querySelectorAll(".compteur input[type='text']");
        
let inputfields = document.querySelectorAll(".compteur input[type='text']");
for(let i =0; i<inputfields.length; i++){
  inputfields[i].addEventListener('input', updateQuantity)
  // l'evenement serait 'change'
  
}

function updateQuantity(e){
    console.log('quantite changé');
    let inputvalue = e.target.value;
    let produit_id = e.target.dataset.product;
    console.log(inputvalue);
    console.log(produit_id);

    const data = {p_id: produit_id, in_val: inputvalue};
    let url = '/shop/updatequantity/'

    fetch(url, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        e.target.closest('.panier').querySelector('.total_panier').innerText = data.montant.toFixed(2);
        e.target.closest('tr').querySelector('.prix_total_article').innerText = data.prix_total.toFixed(2);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}



// let btn = document.querySelector('.add_to_cart');

// btn.addEventListener('click', function(e){
//     e.preventDefault();
//     let product_id = e.target.closest('a').dataset.product
//     let action = e.target.closest('a').dataset.action
//     if(user=='AnonymousUser'){
//       console.log('Ypu are not signed in')
//     }
//     else{
//       addToCart(product_id, action)
//     }
//   })


// function addToCart(p_id, act){
//   const data = {product_id: p_id, action: act};
//     let url = '/shop/updatecart/'
//     fetch(url, {
//     method: 'POST', 
//     headers: {
//         'Content-Type': 'application/json',
//         'X-CSRFToken': csrftoken
//     },
//     body: JSON.stringify(data),
//     })
//     .then(response => response.json())
//     .then(data => {
//     console.log('Success:', data);
//     // document.getElementById('cart').innerHTML = `<h4>${data.quantity}</h4>`
//     })
//     .catch((error) => {
//     console.error('Error:', error);
//     });

// }
