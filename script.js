function uploadAudio() {
  // Get selected file
  let file = document.getElementById("audioFile").files[0];
  if (!file) {
    alert("Please select an audio file first!");
    return;
  }

  // Prepare form data
  let formData = new FormData();
  formData.append("file", file);

  // Send request to backend Flask server
  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    body: formData
  })
  .then(response => {
    if (!response.ok) {
      throw new Error("Server error: " + response.status);
    }
    return response.json();
  })
  .then(data => {
    // Show result on page
    document.getElementById("result").innerText = "Predicted Emotion: " + data.emotion;
  })
  .catch(error => {
    console.error("Error:", error);
    document.getElementById("result").innerText = "Something went wrong!";
  });
}
