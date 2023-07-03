function calculateBMI() {
    var weight = document.getElementById("weight").value;
    var height = document.getElementById("height").value / 100; // Convert height to meters
  
    var bmi = weight / (height * height);
    var result = document.getElementById("result");
  
    if (isNaN(bmi)) {
      result.textContent = "Please enter valid values for weight and height.";
    } else {
      result.textContent = "Your BMI is " + bmi.toFixed(2);
    }
  }

  