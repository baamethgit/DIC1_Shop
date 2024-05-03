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