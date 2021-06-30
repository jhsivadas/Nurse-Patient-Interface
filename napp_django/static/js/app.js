// Targets the mobile menu id for the html
const menu = document.querySelector('#mobile-menu')

// This one targets a class
const menuLinks = document.querySelector('.navbar__menu')

// Display Mobile Menu function
const mobileMenu = () => {
    // Active or not active
    // Toggles the is-active class
    menu.classList.toggle('is-active')
    // Toggles the active class
    menuLinks.classList.toggle('active')
}

menu.addEventListener('click', mobileMenu);

const button = document.querySelector('.btn')
const form   = document.querySelector('.form')

button.addEventListener('click', function() {
   form.classList.add('form--no')
});
