function calculateAge() {
    const dobInput = document.getElementById("dob").value;
    const output = document.getElementById("output");

    if (!dobInput) {
        output.innerHTML = "⚠️ Please select your date of birth!";
        return;
    }

    const dob = new Date(dobInput);
    const today = new Date();

    if (dob > today) {
        output.innerHTML = "⚠️ Future date is not valid!";
        return;
    }

    let years = today.getFullYear() - dob.getFullYear();
    let months = today.getMonth() - dob.getMonth();
    let days = today.getDate() - dob.getDate();

    // Adjust days
    if (days < 0) {
        months--;
        const lastMonth = new Date(today.getFullYear(), today.getMonth(), 0);
        days += lastMonth.getDate();
    }

    // Adjust months
    if (months < 0) {
        years--;
        months += 12;
    }

    output.innerHTML = `🎉 You are ${years} years, ${months} months, and ${days} days old.`;
}