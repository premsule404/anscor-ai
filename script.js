// LOGIN FUNCTION
function login() {

    let email = document.getElementById("email")?.value;
    let password = document.getElementById("password")?.value;

    if (!email || !password) {
        alert("Please enter email and password");
        return;
    }

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

    localStorage.setItem(
        "name",
        document.getElementById("name").value
    );

    localStorage.setItem(
        "email",
        document.getElementById("email").value
    );

    localStorage.setItem(
        "phone",
        document.getElementById("phone").value
    );

    localStorage.setItem(
        "sex",
        document.getElementById("sex").value
    );

    localStorage.setItem(
        "dob",
        document.getElementById("dob").value
    );

    localStorage.setItem(
        "blood",
        document.getElementById("blood").value
    );

    localStorage.setItem(
        "country",
        document.getElementById("country").value
    );

    alert("Signup Successful");
}


// NAVIGATION
function goUpload() {
    window.location.href = "upload.html";
}

function goProfile() {
    window.location.href = "profile.html";
}


// ANALYZE BUTTON
function validateSurvey() {

    let fileInput = document.getElementById("fileInput");

    // CHECK IMAGE
    if (!fileInput || fileInput.files.length === 0) {
        alert("Please upload image first!");
        return;
    }

    // CHECK SYMPTOMS
    let checkboxes = document.querySelectorAll(
        '.symptom-row input[type="checkbox"]'
    );

    let checked = false;

    checkboxes.forEach((box) => {
        if (box.checked) {
            checked = true;
        }
    });

    if (!checked) {
        alert("Please fill symptom survey first!");
        return;
    }

    alert("Survey completed. Now click Submit Symptoms.");
}

async function submitSymptoms() {

    let fileInput =
        document.getElementById("fileInput");

    // CHECK IMAGE

    if (!fileInput || fileInput.files.length === 0) {

        alert("Please upload image first!");

        return;
    }

    // CHECK SYMPTOMS

    let symptoms = [];

    document
        .querySelectorAll(
            '.symptom-row input[type="checkbox"]:checked'
        )
        .forEach((cb) => symptoms.push(cb.value));

    if (symptoms.length === 0) {

        alert("Please select symptoms!");

        return;
    }

    // SAVE SYMPTOMS

    localStorage.setItem(
        "symptoms",
        JSON.stringify(symptoms)
    );

    // FORM DATA

    let formData = new FormData();

    formData.append(
        "image",
        fileInput.files[0]
    );

    try {

    const response = await fetch(
        "http://localhost:5000/predict",
        {
            method: "POST",
            body: formData
        }
    );

    if (!response.ok) {
        throw new Error("Server Error");
    }

    const data = await response.json();

    console.log(data);

    localStorage.setItem(
    "prediction",
    data.result
);

localStorage.setItem(
    "confidence",
    data.confidence
);

localStorage.setItem(
    "hemoglobin",
    data.hemoglobin
);

    localStorage.setItem(
        "uploadedImage",
        URL.createObjectURL(fileInput.files[0])
    );

    alert("Prediction Success!");

    window.location.href = "result.html";

} catch (error) {

    console.error(error);

    alert("Backend connection failed!");

}
}

// RESULT ANALYSIS
function analyzeSymptoms() {

    const symptoms =
        JSON.parse(
            localStorage.getItem("symptoms")
        ) || [];

    let result = "";

    const count = symptoms.length;

    if (count >= 6) {

        result =
            "⚠ High possibility of Anemia. Please consult a doctor immediately.";

    } else if (count >= 3) {

        result =
            "⚠ Moderate symptoms detected. Monitor your health.";

    } else if (count > 0) {

        result =
            "🟡 Mild symptoms detected.";

    } else {

        result =
            "🟢 No major symptoms detected.";
    }

    result +=
        "\n\nSelected Symptoms: " +
        symptoms.join(", ");

    let resultText =
        document.getElementById("resultText");

    if (resultText) {
        resultText.innerText = result;
    }
}

// AUTO LOAD RESULT DATA
window.onload = function () {

    let prediction =
        localStorage.getItem("prediction");

    let uploadedImage =
        localStorage.getItem("uploadedImage");

    let resultText =
        document.getElementById("resultText");

    let resultImage =
        document.getElementById("resultImage");

    if (prediction && resultText) {

        if (
            prediction.toLowerCase().includes("anemic")
        ) {

            resultText.innerHTML =
                "Potential Anemia Indicated";

        } else {

            resultText.innerHTML =
                "No Anemia Detected";
        }
    }

    if (uploadedImage && resultImage) {
        resultImage.src = uploadedImage;
    }

    analyzeSymptoms();
};

window.onload = function () {

    let prediction =
        localStorage.getItem("prediction");

    let image =
        localStorage.getItem("uploadedImage");

    let result =
        document.getElementById("predictionResult");

    let img =
        document.getElementById("resultImage");

    if (result) {
        result.innerText =
            "Prediction: " + prediction;
    }

    if (img) {
        img.src = image;
    }
};

let username = localStorage.getItem("name");

document.getElementById(
    "patientName"
).innerText = username || "User";

let patientId =
    "P" + Math.floor(Math.random() * 100000);

document.getElementById(
    "patientId"
).innerText = patientId;

let today = new Date();

document.getElementById(
    "examDate"
).innerText =
    today.toDateString();


let dob = localStorage.getItem("dob");

if (dob) {

    let birthDate = new Date(dob);

    let today = new Date();

    let years =
        today.getFullYear() -
        birthDate.getFullYear();

    let months =
        today.getMonth() -
        birthDate.getMonth();

    let days =
        today.getDate() -
        birthDate.getDate();

    if (days < 0) {
        months--;
        days += 30;
    }

    if (months < 0) {
        years--;
        months += 12;
    }

    document.getElementById(
        "fullAge"
    ).innerHTML =
        "<b>Age:</b> " +
        years + " Years " +
        months + " Months " +
        days + " Days";
}
