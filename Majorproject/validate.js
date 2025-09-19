function validateForm() {
  let name = document.getElementById("name").value.trim();
  let email = document.getElementById("email").value.trim();
  let age = document.getElementById("age").value;

  if (name === "" || email === "" || age === "") {
    alert("All fields are required!");
    return false;
  }
  if (age < 0 || age > 100) {
    alert("Enter valid age!");
    return false;
  }
  return true;
}
