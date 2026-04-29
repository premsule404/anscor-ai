// LOGIN FUNCTION
function login() {
    let email = document.getElementById("email")?.value;
    let password = document.getElementById("password")?.value;

    if (!email || !password) {
        alert("Please enter email and password");
        return;
    }

    // (Temporary - no backend auth yet)
    alert("Login Successful");
    window.location.href = "home.html";
}


// SIGNUP FUNCTION
function signup() {
    let name = document.getElementById("name")?.value;
    let email = document.getElementById("email")?.value;
    let phone = document.getElementById("phone")?.value;
    let password = document.getElementById("password")?.value;

    if (!name || !email || !phone || !password) {
        alert("Please fill all fields");
        return;
    }

    // Save data locally (for demo)
    localStorage.setItem("name", document.getElementById("name").value);
    localStorage.setItem("email", document.getElementById("email").value);
    localStorage.setItem("phone", document.getElementById("phone").value);

    localStorage.setItem("sex", document.getElementById("sex").value);
    localStorage.setItem("dob", document.getElementById("dob").value);
    localStorage.setItem("age", document.getElementById("age").value);
    localStorage.setItem("blood", document.getElementById("blood").value);
    localStorage.setItem("country", document.getElementById("country").value);

    alert("Registered!");
    window.location.href = "login.html";
}

// NAVIGATION
function goUpload() {
    window.location.href = "upload.html";
}

function goProfile() {
    window.location.href = "profile.html";
}


// IMAGE UPLOAD FUNCTION
async function upload() {
    let fileInput = document.getElementById("fileInput");
    let file = fileInput.files[0];

    if (!file) {
        alert("Please select image");
        return;
    }

    let formData = new FormData();
    formData.append("file", file);

    try {
        let response = await fetch("http://127.0.0.1:5000/upload", {
            method: "POST",
            body: formData
        });

        let data = await response.json();

        document.getElementById("result").innerText = data.result;

    } catch (error) {
        console.error(error);
        alert("Error connecting to backend");
    }
}
