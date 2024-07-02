$(document).ready(function () {
    $('#form-register').submit(function (e) {
        e.preventDefault();
        let passwordRegister = $("#pass").val();
        let verifyPassword = $("#verifyPass").val();
        let user = $('#usuarioRegistro').val();
        let userTrim = $.trim(user);

        let codCountry = $('#codPais').val();
        let phone = $('#phone').val();

        if (userTrim.length < 5 || userTrim.length > 20) {
            $('#messageUsuario').text('Ingresa tu nombre de usuario (debe tener entre 5 y 20 caracteres)').fadeIn();
            return false;
        } else if (userTrim.indexOf(' ') >= 0) {
            $('#messageUsuario').text('El nombre de usuario no puede contener espacios').fadeIn();
            return false;
        } else {
            $('#messageUsuario').fadeOut();
        }

        let email = $('#emailRegistro').val();

        if (email == '') {
            $('#messageEmail').text('El campo de correo no puede estar vacío').fadeIn();
            return false;
        } else if (email.indexOf(' ') >= 0) {
            $('#messageEmail').text('El correo electrónico no puede contener espacios').fadeIn();
            return false;
        } else if (!isEmail(email)) {
            $('#messageEmail').text('El correo electrónico no es válido, ocupa @ y dominio').fadeIn();
            return false;
        } else {
            $('#messageEmail').fadeOut();
        }

        if (phone !== "" && codCountry === "+56" && !isChile(phone)) {
            $('#messagePhone').text('El número móvil de Chile comienza con 9').fadeIn();
            return false;
        } else {
            $('#messagePhone').fadeOut();
        }

        if (passwordRegister == '') {
            $('#messagePassword').text('La contraseña no puede estar vacía').fadeIn();
            return false;
        } else if (!isPass(passwordRegister)) {
            $('#messagePassword').text('La contraseña debe tener al menos una mayúscula, una minúscula, un número y un carácter especial(. / - @)').fadeIn();
            return false;
        } else {
            $('#messagePassword').fadeOut();
        }

        if (verifyPassword == '') {
            $('#messageConfirm').text('Confirma la contraseña').fadeIn();
            return false;
        } else if (verifyPassword !== passwordRegister) {
            $('#messageConfirm').text('Las contraseñas deben coincidir').fadeIn();
            return false;
        } else {
            $('#messageConfirm').fadeOut();
        }

        if (!$('#formCheck').prop('checked')) {
            $('#checkeado').text('Acepta los términos y condiciones para continuar').fadeIn();
            return false;
        } else {
            $('#checkeado').fadeOut();
        }

        // Alerta Sweet
        Swal.fire({
            title: 'Registro Exitoso',
            text: '¡Tu registro ha sido completado con éxito!',
            icon: 'success',
            confirmButtonText: 'Iniciar Sesión',
            timer: 6000
        }).then((result) => {
            if (result.isConfirmed) {
                window.location.href = '../mce/login';
            } else {
                $('form').unbind('submit').submit();
            }
        });
    });

    function isEmail(emailTrim) {
        const emailRegex = /^[a-zA-Z0-9_.-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$/;
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