import React, { useState } from "react";
import "./Register.css";

const Register = () => {
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const register_url = window.location.origin + "/djangoapp/register";

  const register = async (e) => {
    e.preventDefault();

    if (!userName || !password || !email || !firstName || !lastName) {
      setErrorMessage("All five input fields are required.");
      return;
    }

    try {
      const res = await fetch(register_url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          userName: userName,
          password: password,
          firstName: firstName,
          lastName: lastName,
          email: email,
        }),
      });

      const json = await res.json();
      if (json.status === "Authenticated") {
        sessionStorage.setItem("username", json.userName);
        window.location.href = window.location.origin;
      } else if (json.error === "Already Registered") {
        setErrorMessage("The username is already taken. Please pick another.");
      } else {
        setErrorMessage(json.error || "Registration failed. Please check details.");
      }
    } catch (err) {
      setErrorMessage("Error connecting to registration backend service.");
    }
  };

  return (
    <div className="register_container">
      <div className="register_header">
        <span className="text_header">Sign Up</span>
        <div className="underline"></div>
      </div>
      <form onSubmit={register} className="inputs_wrapper">
        {errorMessage && <div className="error_message">{errorMessage}</div>}

        {/* 1. Username Field */}
        <div className="input_box">
          <label className="input_label">Username</label>
          <input
            type="text"
            name="username"
            placeholder="Choose username"
            className="input_field"
            value={userName}
            onChange={(e) => setUserName(e.target.value)}
            required
          />
        </div>

        {/* 2. First Name Field */}
        <div className="input_box">
          <label className="input_label">First Name</label>
          <input
            type="text"
            name="first_name"
            placeholder="First Name"
            className="input_field"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            required
          />
        </div>

        {/* 3. Last Name Field */}
        <div className="input_box">
          <label className="input_label">Last Name</label>
          <input
            type="text"
            name="last_name"
            placeholder="Last Name"
            className="input_field"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            required
          />
        </div>

        {/* 4. Email Field */}
        <div className="input_box">
          <label className="input_label">Email Address</label>
          <input
            type="email"
            name="email"
            placeholder="Email Address"
            className="input_field"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>

        {/* 5. Password Field */}
        <div className="input_box">
          <label className="input_label">Password</label>
          <input
            type="password"
            name="password"
            placeholder="Password"
            className="input_field"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>

        {/* Submit / Register Button */}
        <div className="submit_section">
          <button type="submit" className="register_button">
            Register
          </button>
        </div>
      </form>
    </div>
  );
};

export default Register;
