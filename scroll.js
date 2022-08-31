let arrow = document.getElementById('scrollToCards'); // arrow bind

arrow.onclick = function scrollToCards(e) {
    window.scroll({
        left: 0,
        top: e.offsetTop,
        behavior: 'smooth'
    })

    let cards = arrow;

    scrollToCards(cards)

}
// let info = document.getElementById('info'); // 'our services' bind

// info.onclick = arrow.onclick

// let consult = document.getElementById('consult'); // 'order consultation' bind

// consult.onclick = function scrollToForm(e) {
//     window.scroll({
//         left: 0,
//         top: e.offsetTop,
//         behavior: 'smooth'
//     })

//     let form = document.getElementById('form');

//     scrollToForm(form)
// }