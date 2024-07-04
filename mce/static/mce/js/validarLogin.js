$(document).ready(function () {
  $('#form-login').on("submit", function (e) {
    let isValid = true;
    let passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[./@-]).{8,}$/;
    let username = $('#username').val();

    if (username.length < 5 || username.length > 20) {
      $('#messageLogin').text('Ingresa tu nombre de usuario (debe tener entre 5 y 20 caracteres)').fadeIn();
      isValid = false;
    } else if (username.indexOf(' ') >= 0) {
      $('#messageLogin').text('El nombre de usuario no puede contener espacios').fadeIn();
      isValid = false;
    } else {
      $('#messageLogin').fadeOut();
    }

    let password = $('#password').val();

    if (password == '') {
      $('#messagePass').text('La contraseña no puede estar vacía').fadeIn();
      isValid = false;
    } else if (!passwordRegex.test(password)) {
      $('#messagePass').text('La contraseña debe tener al menos una mayúscula, una minúscula, un número y un carácter especial: . / - @').fadeIn();
      isValid = false;
    } else {
      $('#messagePass').fadeOut();
    }

    if (!isValid) {
      e.preventDefault();
    } else {
      $('#btnLogin').prop('disabled', true);
      Swal.fire({
        title: '¡Bienvenido!',
        text: 'Credenciales correctas',
        icon: 'success',
        confirmButtonText: 'CONTINUAR',
        timer: 6000
      }).then((result) => {
        if (result.isConfirmed) {
          window.location.href = '../mce/index';
        }
      });
    }
  });

  $('#username').on('input', function () {
    let username = $(this).val();
    if (username.length > 20) {
      $(this).val(username.substr(0, 20));
      alert('Solo se permiten 20 caracteres');
    }
  });
});
