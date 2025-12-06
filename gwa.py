from js import document

# FROM SW2
def calculate_gwa(event=None):
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    subjects = ["science", "math", "english", "filipino", "ict", "pe"]
    grades = [float(document.getElementById(subj).value or 0) for subj in subjects]

    gwa = round(sum(grades) / len(grades), 2)
    remarks_list = ["FAILED ❌", "PASSED ✅"]
    remarks = remarks_list[int(gwa >= 75)]

    result = (
        f"Student: {first_name} {last_name}\n"
        f"Average Grade (GWA): {gwa}\n"
        f"Remarks: {remarks}"
    )

    document.getElementById("result").innerText = result

document.getElementById("calc_btn").onclick = calculate_gwa
