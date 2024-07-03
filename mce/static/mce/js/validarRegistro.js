$(document).ready(function () {
    $('#form-register').on('submit', function (event) {
        let isValid = true;
        $('.error').hide();

        let username = $('#username').val().trim();
        let codCountry = $('#codPais').val();
        let phone = $('#phone').val();
        if (username === '') {
            isValid = false;
            $('#messageUsuario').text('Ingrese un nombre de usuario válido').fadeIn();
        } else if (username.length < 5 || username.length > 20) {
            isValid = false;
            $('#messageUsuario').text('El nombre de usuario debe tener entre 5 y 20 caracteres').fadeIn();
        } else {
            $('#messageUsuario').fadeOut();
        }

        let email = $('#email').val().trim();
        if (email === '') {
            isValid = false;
            $('#messageEmail').text('Ingrese un correo electrónico válido').fadeIn();
        } else if (!isEmail(email)) {
            isValid = false;
            $('#messageEmail').text('Formato de correo electrónico incorrecto').fadeIn();
        } else {
            $('#messageEmail').fadeOut();
        }

        if (phone !== "" && codCountry === "+56" && !isChile(phone)) {
            isValid = false;
            $('#messagePhone').text('El número móvil de Chile comienza con 9').fadeIn();
        } else {
            $('#messagePhone').fadeOut();
        }

        let passwordRegister = $('#pass').val().trim();
        if (passwordRegister === '') {
            isValid = false;
            $('#messagePassword').text('Ingrese una contraseña válida').fadeIn();
        } else if (!isPass(passwordRegister)) {
            isValid = false;
            $('#messagePassword').text('La contraseña debe tener al menos una mayúscula, una minúscula, un número y un carácter especial (. / @)').fadeIn();
        } else {
            $('#messagePassword').fadeOut();
        }

        let verifyPassword = $('#verifyPass').val().trim();
        if (verifyPassword === '') {
            isValid = false;
            $('#messageConfirm').text('Confirme la contraseña').fadeIn();
        } else if (verifyPassword !== passwordRegister) {
            isValid = false;
            $('#messageConfirm').text('Las contraseñas no coinciden').fadeIn();
        } else {
            $('#messageConfirm').fadeOut();
        }

        if (!$('#formCheck').prop('checked')) {
            isValid = false;
            $('#checkeado').text('Acepta los términos y condiciones para continuar').fadeIn();
        } else {
            $('#checkeado').fadeOut();
        }

        if (!isValid) {
            event.preventDefault();
        } else {

            Swal.fire({
                title: 'Registro Exitoso',
                text: '¡Tu registro ha sido completado con éxito!',
                icon: 'success',
                confirmButtonText: 'Iniciar Sesión',
                timer: 6000
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = '../mce/loginC';
                } else {
                    $('#form-register').off('submit').submit();
                }
            });
        }
    });

    function isEmail(emailTrim) {
        const emailRegex = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;
        return emailRegex.test(emailTrim);
    }

    function isPass(pass) {
        const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[./@-]).{8,}$/;
        return passwordRegex.test(pass);
    }

    function isChile(phone) {
        const phoneRegex = /^9\d{8}$/;
        return phoneRegex.test(phone);
    }

    $('#phone').on('input', function () {
        let phone = $(this).val();
        if (phone.length > 9) {
            $(this).val(phone.substr(0, 9));
        }
    });
});