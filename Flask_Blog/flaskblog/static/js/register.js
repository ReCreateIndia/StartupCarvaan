const form = document.getElementById('query');

//UPLOAD FILE
function upload(){
    //get your select image
    var image = document.getElementById("image").files[0];
    //now get your image name
    var imageName = image.name;
    //firebase storage reference
    //it is the path where your image will store
    var storageRef = firebase.storage().ref('Idea/'+ imageName);
    //upload image to selected storage reference 
    var uploadTask = storageRef.put(image);

    uploadTask.on('state_changed', function(snapshot){
        //observe state change events such as progress, pause, resume
        document.getElementById("upload").textContent = "Please Wait While Uploading...";
        var progress = (snapshot.bytesTransferred/snapshot.totalBytes)*100;
        if(progress === 100){
            document.getElementById("upload").textContent = "Uploaded Successfully";
        }
    },function(error){
        console.log(error.message);
    },function(){
        uploadTask.snapshot.ref.getDownloadURL().then(function(downloadURL){
            console.log(document.getElementById("pic").value);
            document.getElementById("pic").value =  downloadURL;
            console.log(downloadURL);
        });
    });
}

// saving Data
form.addEventListener('submit', (e) => {
    e.preventDefault();
    db.collection('Register').add({
        TeamName: form.Team.value,
        Email: form.Email.value,
        PhoneNumber: form.Phone.value,
        Idea: form.Idea.value,
        Select: form.choose.value
    }).then(()=>{
        console.log("upload successful")
    })
    form.Team.value = '';
    form.Email.value = '';
    form.Phone.value = '';
    form.Idea.value = '';
})
