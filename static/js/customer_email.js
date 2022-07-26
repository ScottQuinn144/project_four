function sendMail(contactForm) {
    emailjs.send("service_1merlqf", "template_ekl3vdo", {
            "from_name": contactForm.name.value,
            "message": contactForm.query.value,
            "from_email": contactForm.emailaddress.value
        })
        .then(
            function (response) {
                console.log("SUCCESS", response);
                window.location.href = '../'

            },
            function (error) {
                console.log("FAILED", error);
                window.location = 'contact.html';
            }
        );
    return false;
}
