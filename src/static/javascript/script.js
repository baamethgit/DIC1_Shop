const frais = document.querySelector('.frais')//.innerText;
const taxes = document.querySelector('.taxes')//.innerText;


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
  inputfields[i].addEventListener('input', updateQuantity);
//   let totalePanier = document.querySelector('.panier .total_panier').innerText
//   let montantFinale = parseFloat(totalePanier) - parseFloat(frais) - parseFloat(taxes);
//   document.querySelector('.panier .total_panier_avec_frais').innerText = montantFinale.toFixed(2).toString().replace('.', ',');
  if (inputfields[i].value == '01'){
    // inputfields[i].closest('div').querySelector('.bi-dash')
  }
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
        e.target.closest('.panier').querySelector('.total_panier').innerText = data.montant.toFixed(2).toString().replace('.', ',');
        e.target.closest('tr').querySelector('.prix_total_article').innerText = data.prix_total.toFixed(2).toString().replace('.', ',');
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
