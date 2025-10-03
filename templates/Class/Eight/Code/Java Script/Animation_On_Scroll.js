// =================================================================

const observer = new IntersectionObserver((Animation_On_Scroll) => {
    Animation_On_Scroll.forEach((Gps_Scroll) => {
        console.log(Gps_Scroll);
        if (Gps_Scroll.isIntersecting) {
            Gps_Scroll.target.classList.add("show");
        } else {
            Gps_Scroll.target.classList.remove("show");
        }
    });
});

// =================================================================

// =================================================================

const Payeh = document.querySelectorAll(".Payeh");
Payeh.forEach((Animation_On_Scroll_By_Css_JavaScript) =>
    observer.observe(Animation_On_Scroll_By_Css_JavaScript));
// =================================================================

const Tozih = document.querySelectorAll(".Tozih");
Tozih.forEach((Animation_On_Scroll_By_Css_JavaScript) =>
    observer.observe(Animation_On_Scroll_By_Css_JavaScript));
// =================================================================

const Img_7 = document.querySelectorAll(".Img_7");
Img_7.forEach((Animation_On_Scroll_By_Css_JavaScript) =>
    observer.observe(Animation_On_Scroll_By_Css_JavaScript));
// =================================================================

const Lets_To_Seven = document.querySelectorAll(".Lets_To_Seven");
Lets_To_Seven.forEach((Animation_On_Scroll_By_Css_JavaScript) =>
    observer.observe(Animation_On_Scroll_By_Css_JavaScript));
// =================================================================