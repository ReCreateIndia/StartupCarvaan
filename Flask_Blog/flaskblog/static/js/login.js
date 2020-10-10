// var firebaseConfig = {

//   };
  // Initialize Firebase
//   var firebaseConfig="{{firebaseConfig}}";
//   firebase.initializeApp(firebaseConfig);
  firebase.auth.Auth.Persistence.LOCAL
  auth=firebase.auth()
  
  function SeedDB()
  {
      var email = $("#uname").val();
      var password = $("#pass").val();
      if(email != "" && password != "")
    {
        document.getElementById("final").textContent = "Logging You In...";
        console.log("inside");
        firebase.auth().signInWithEmailAndPassword(email, password).then(function() {
            console.log('hit finally');
            console.log(firebase.auth().currentUser);
            window.location.href = "/login/index.html";
            
        }).catch(function(error)
        {
            document.getElementById("final").textContent = "Wrong Credential";
            console.log('hit hahah');
            var errorCode = error.code;
            var errorMessage = error.message;

            console.log(errorCode);
            console.log(errorMessage);
            window.alert("Message : " + errorMessage);
        });
            console.log("present");
    }
    else
    {
        window.alert("Form is incomplete . Please fill out all fields.");
    }
  }
  
  
