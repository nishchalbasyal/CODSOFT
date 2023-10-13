$(document).ready(function () {
  $(".reply-form").hide();
  $(".error").hide();
  $(".register-error").hide();
});

const login_func = () => {
    window.location.href = "/login";
  }

const logout_func = () => {
    window.location.href = "/logout";
};

const write_func = (isLogin) => {
  if (isLogin) {
    window.location.href = "/write";
  } else {
    window.location.href = "/login";
  }
};

const single_post_func = (slug) => {
  console.log(slug);
  if (slug) {
    window.location.href = `/${slug}`;
  } else {
    window.location.href = "/";
  }
};
const single_post_edit_func = (slug) => {
  console.log(slug);
  if (slug) {
    window.location.href = `/${slug}/update`;
  } else {
    window.location.href = "/";
  }
};
const single_post_delete_func = (slug) => {
  console.log(slug);
  if (slug) {
    window.location.href = `/delete/${slug}`;
  } else {
    window.location.href = "/";
  }
};

let comment;
let commentReply;

function handleCommentReplyChange(value) {
  commentReply = value;
}

function handleCommentChange(value) {
  comment = value;
}
function handleFollowhandler(currentUser, author) {
    
  fetch(`/author/${author}?currentUser=${currentUser}&author=${author}`)
  .then(response => {
    if (response.ok) {
      return response.json(); // Parse the response as JSON
    } else {
      throw new Error('Request failed');
    }
  })
  .then(data => {
    // Handle the JSON response data here
    const followBtn = document.getElementById('followBtn');

    if (data.status === 'followed') {
      // Update button text to "Unfollow"
      followBtn.textContent = 'Unfollow';
    } else if (data.status === 'unfollowed') {
      // Update button text to "Follow"
      followBtn.textContent = 'Follow';
    }
  })
  .catch(error => {
    console.error('Error', error);
  });

}




/* Comments Section code */
$(".ready-reply").click(function () {
  let commentCard = $(this).closest(".comment-card");
  let replyForm = commentCard.find(".reply-form");

  replyForm.show();
  $(this).hide();
});


$(".final-reply").click(function () {
  event.preventDefault();
  let commentCard = $(this).closest(".comment-card");
  let replyForm = commentCard.find(".reply-form");
  let replyComment = commentCard.find(".reply-comment").val();
  let commentID = replyForm.data("comment-id")
  let csrf = $("#csrfToken").val()
  console.log(csrf)

  let payload = JSON.stringify({
    comment: replyComment,
    commentID:commentID
  });

 


  $.ajax({
    url: "/post/comment/reply",
    method: "POST",
    headers: { "X-CSRFToken": csrf },
    data: payload,
    dataType: "json",
  })
    .done(function (response) {
      console.log(response.id + " " + response.name);
      window.location.reload();

    })
    .fail(function (error) {
      console.log(error);
    });
   
  location.reload()
  replyForm.hide();
  commentCard.find(".ready-reply").show();
});


$(".login-reply").click(function(event){
    window.location.href = "/login"
})

/**********Login  */

// $("#login-btn").click(function (event) {
//   event.preventDefault();
//   let email = $(".login-form").find("#email").val();
//   let password = $(".login-form").find("#password").val();

//   let regex = /^([_\-\.0-9a-zA-Z]+)@([_\-\.0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/;

//   let errorMessage = "";

//   if (email.trim() === "") {
//     errorMessage = "missing email Field";
//     $(".error").show();
//     $(".error-email").text(errorMessage);
//   } else if (!regex.test(email)) {
//     errorMessage = "invalid email";
//     $(".error").show();
//     $(".error-email").text(errorMessage);
//   } else if (password.trim() === "") {
//     $(".error").show();
//     errorMessage = "missing Password Field";
//     $(".error-password").text(errorMessage);
//   } else {
//     $(".error").hide();
//   }

//   if (!errorMessage) {
//     $(".llogin-form").submit();
//   }
// });



/******** Register ******* */

let email_error = true;
function email_validation() {
  let email = $("#eemail").val();
  let regex = /^([_\-\.0-9a-zA-Z]+)@([_\-\.0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/;

  if (email.length == 0) {
    $(".register-email-error").show();
    $(".register-email-error").text("** please enter email");
    email_error = true;
    return false;
  } else if (!regex.test(email)) {
    $(".register-email-error").show();
    $(".register-email-error").text("** email is invalid");
    email_error = true;
    return false;
  } else {
    $(".register-email-error").hide();
    email_error = false;
    return true;
  }
}

let password_error = true;
function passwordError() {
  let password = $("#ppassword").val();

  if (password.length < 4 || password.length > 20) {
    $(".register-password-error").show();
    $(".register-password-error").text(
      "password length must be between 4 and 20"
    );
    password_error = true;
    return false;
  } else {
    $(".register-password-error").hide();
    password_error = false;
    return true;
  }
}

let fullname_error = true;
function fullnameError() {
  let fullname = $("#ffullname").val();

  if (
    fullname.length == 0 ||
    fullname == "" ||
    fullname == null ||
    fullname == undefined
  ) {
    $(".register-fullname-error").show();
    $(".register-fullname-error").text("name must not be empty");
    fullname_error = true;
    return false;
  } else {
    $(".register-fullname-error").hide();
    fullname_error = false;
    return true;
  }
}


function file_validation() {
  let file = $("#ffile")[0].files[0];
 
  let maxSize = 3 * 1024 * 1024;

  if (file.type !== "image/png" && file.type !== "image/jpg" && file.type !== "image/jpeg") {
    $(".register-file-error").show();
    $(".register-file-error").text("image must be in 'png' or 'jpg' format");
    return false;
  } else if (file.size > maxSize) {
    $(".register-file-error").show();
    $(".register-file-error").text("image size must be less than 3 mb");
    return false;
  } else {
    $(".register-file-error").hide();
    return true;
  }
}

$("#sign-up").click(function (event) {
  event.preventDefault();
  if (email_validation() && passwordError() && fullnameError() && file_validation()) {
    $(".register-form").submit();
  }
});


 
