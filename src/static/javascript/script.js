document.addEventListener("DOMContentLoaded", function() {
// Inscription-Connexion


// Page produits / categories

    
// Barre de recherche
    let searchBar = document.querySelector('.search_bar');
    if (searchBar){
        let submitBtn = searchBar.querySelector('button[type="submit"]');
        let input = searchBar.querySelector('input[type="search"]');
        if (!input.value){
            submitBtn.disabled = true
        }else{
            submitBtn.disabled = false
        }
        input.addEventListener('input',(e)=>{
            if (!input.value){
                submitBtn.disabled = true
            }else{
                submitBtn.disabled = false
            }
        })
    }

    // affichage des categories à l'aide de radio button
    const listeRadioBtns=document.querySelectorAll(".liste_categories input[type=radio]");
    for( radioBtn of listeRadioBtns){
        // Gestion des liens
      radioBtn.addEventListener('click', function(e){
            let link = e.target.closest('a');
            let url = link.getAttribute('href')
            window.open(url, "_top");
        })

        //  changement de style(responsivite )
        const display = window.getComputedStyle(radioBtn, null).getPropertyValue("display");
        if (radioBtn.checked && display == 'none'){// si le btn,en plus d'etre checked est masqué (petits ecrans)
            let link = radioBtn.closest('a');
            link.style.backgroundColor = "#1b6392";   
            link.style.color = "white";
        }
    }
    // le changement de style lorsqu'on reduit / augmente la taille de l'écran
    window.addEventListener('resize', function() {
        for(radioBtn of listeRadioBtns){
            let a = radioBtn.closest('a');
            const display = window.getComputedStyle(radioBtn, null).getPropertyValue("display");
            if (radioBtn.checked && display == 'none'){
                a.style.backgroundColor = "#1b6392";   
                a.style.color = "white";
            }
            else{
                a.style.backgroundColor = "initial";   
                a.style.color = "initial";
            }
        }
    })
    // Le select de catégories pour les peties écrans
    const selectCategorie=document.querySelector(".liste_categories select");
    if (selectCategorie){ // pour éviter des erreurs si on est sur d'autres pages qui n'ont pas le select(null)
        selectCategorie.addEventListener('change', (event) => {
            const optionValue = event.target.value;
            let url;
            if (optionValue === ''){// <=> toutes les catégories
                url = '/';
            }else{
                url = '/shop/produits/categories/'+optionValue; // optionValue correspond au slug de la catégorie
            }
            window.open(url, "_top");
        });
    };


// PANIER ET DETAIL PRODUIT

    // Button plus et moins

        // tous les btns + pour prendre en compte toutes les compteurs
        const plusBtns = document.querySelectorAll(".compteur .bi-plus");
        const minusBtns = document.querySelectorAll(".compteur .bi-dash");
        const inputCompteur = document.querySelectorAll(".compteur input[type='text']");

        function formatInt(number) { // affichage de nombre
            number = parseInt(number, 10);
            if (number < 10) {
                return '0' + number;
            }
            return number;
        }
        function incrementerCompteur(index) {
            let value = parseInt(inputCompteur[index].value, 10);
            if (!isNaN(value)) {
                value++;
                inputCompteur[index].value = formatInt(value);
            }
        }
        function decrementerCompteur(index) {
            let value = parseInt(inputCompteur[index].value, 10);
            if (!isNaN(value) && value > 1) {
                value--;
                inputCompteur[index].value = formatInt(value);
            }
        }
        // affichage initial des valeurs du compteur
        inputCompteur.forEach((input, index) => {
            input.value = formatInt(input.value);
        })

        // ajout des evenements aux btns plus et moins
        plusBtns.forEach((plusBtn, index) => {
            plusBtn.addEventListener("click", function() {
                incrementerCompteur(index);
                inputCompteur[index].dispatchEvent(new Event('input')); //déclencher un événement input sur l'élément 
            });
        });
        minusBtns.forEach((minusBtn, index) => {
            minusBtn.addEventListener("click", function() {
                decrementerCompteur(index);
                inputCompteur[index].dispatchEvent(new Event('input'));
            });
        });

        // Mis à jour de la quantité d'un article à partir de l'input (panier).
        let inputfields = document.querySelectorAll(".panier .compteur input[type='text']");
        for(let i =0; i<inputfields.length; i++){
            inputfields[i].addEventListener('input',updateQuantity);
        }
        function updateQuantity(e){
            let inputvalue = e.target.value;
            let produit_id = e.target.dataset.produit;
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
                e.target.closest('.panier').querySelector('.total_panier').innerText = data.montant.toFixed(2).toString().replace('.', ',');
                e.target.closest('tr').querySelector('.prix_total_article').innerText = data.prix_total_article.toFixed(2).toString().replace('.', ',');
                e.target.closest('.panier').querySelector('.total_panier_avec_frais').innerText = data.montant_total.toFixed(2).toString().replace('.', ',');
                document.querySelector('.nb_article').innerText = data.quantite_panier;
            })  
            .catch((error) => {
                console.error('Error:', error);
            });
        }

    let deleteBtns = document.querySelectorAll(".supprimer_article i");
    for(let i =0; i<deleteBtns.length; i++){
        deleteBtns[i].addEventListener('click', supprimerArticle);
    }
    function supprimerArticle(e){
        let article_id = e.target.closest('span').dataset.article;
        const data = {a_id: article_id};
        let url = '/shop/panier/supprimer_article/'
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
            e.target.closest('.panier').querySelector('.total_panier').innerText = data.montant.toFixed(2).toString().replace('.', ',');
            e.target.closest('.panier').querySelector('.total_panier_avec_frais').innerText = data.montant_total.toFixed(2).toString().replace('.', ',');
            document.querySelector('.nb_article').innerText = data.quantite_panier;
            e.target.closest('tr').style.display = 'none';
            let trs = document.querySelectorAll('table tr');
            let ligneVisible = 0;
            for(let i = 1; i < trs.length; i++) {
                let row = trs[i];
                if (row.style.display !== 'none') {
                    ligneVisible++;
                    break;
                }
            }
            if (ligneVisible === 0) {
                let submitBtn = document.querySelector(".panier input[type='submit']");
                submitBtn.disabled = true;
                e.target.closest('.panier').querySelector('.total_panier_avec_frais').innerText = data.montant.toFixed(2).toString().replace('.', ',');
            }
            })
        .catch((error) => {
            console.error('Error:', error);
        });
    }

// Application Account
    // afficher/masquer mot de passe
    function togglePassword(passwordInput){
        const type = passwordInput.getAttribute('type');
            if (type === 'password'){
                passwordInput.setAttribute('type','text');
            }else if(type === 'text'){
                passwordInput.setAttribute('type','password');
            }
    }

    let btns_toggle_password = document.querySelectorAll('.input-group-text');
    btns_toggle_password.forEach((btn, index) => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            if (e.target.closest('.input-group')){
                const passwordInput = e.target.closest('.input-group').querySelector('.form-control');
                togglePassword(passwordInput);
            }else{
                const passwordInputs = e.target.closest('form').querySelectorAll(".password_input");
                togglePassword(passwordInputs[index]); 
            }  
        })
    })



});
