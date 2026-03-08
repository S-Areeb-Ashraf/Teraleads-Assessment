# Section 2

import json

APPOINTMENTS_JSON = """
[
    {
        "id": "APT-001",
        "patient_name": "Sarah Mitchell",
        "phone": "+1-555-204-3871",
        "appointment_date": "Monday, March 10th",
        "appointment_time": "10:30 AM",
        "provider": "Dr. Elena Reyes",
        "service": "dental consultation",
        "clinic_name": "Bright Smile Dental",
        "confirmation_code": "DS-8821"
    },
    {
        "id": "APT-002",
        "patient_name": "James Okafor",
        "phone": "+1-555-317-9042",
        "appointment_date": "Tuesday, March 11th",
        "appointment_time": "2:00 PM",
        "provider": "Dr. Marcus Webb",
        "service": "orthodontic follow-up",
        "clinic_name": "Bright Smile Dental",
        "confirmation_code": "DS-8834"
    },
    {
        "id": "APT-003",
        "patient_name": "Linda Chávez",
        "phone": "+1-555-489-6610",
        "appointment_date": "Wednesday, March 12th",
        "appointment_time": "9:00 AM",
        "provider": "Dr. Elena Reyes",
        "service": "teeth whitening session",
        "clinic_name": "Bright Smile Dental",
        "confirmation_code": "DS-8847"
    }
]
"""

def generate_reminder(appointment_data: dict) -> str:
    name       = appointment_data["patient_name"]
    date       = appointment_data["appointment_date"]
    time       = appointment_data["appointment_time"]
    provider   = appointment_data["provider"]
    service    = appointment_data["service"]
    clinic     = appointment_data["clinic_name"]
    code       = appointment_data["confirmation_code"]

    message = (
        f"<friendly tone> "
        f"Hello, {name}! <pause: 300ms> "
        f"This is a friendly reminder from {clinic}. <pause: 500ms> "
        f"You have an upcoming {service} scheduled for {date} at {time} "
        f"with {provider}. <pause: 400ms> "
        f"Your confirmation code is <slow pace> {code}. <pause: 300ms> "
        f"<resume pace> If you need to reschedule or have any questions, "
        f"please call us at your earliest convenience. <pause: 400ms> "
        f"We look forward to seeing you. Have a wonderful day! <warm close>"
    )
    return message


def main():
    appointments = json.loads(APPOINTMENTS_JSON)

    print("=" * 65)
    print("  TERALEADS – TTS APPOINTMENT REMINDER MESSAGES")
    print("=" * 65)

    for appt in appointments:
        reminder = generate_reminder(appt)
        print(f"\n[Appointment ID: {appt['id']}]")
        print(f"Patient : {appt['patient_name']}")
        print(f"Phone   : {appt['phone']}")
        print(f"\nGenerated TTS Message:")
        print("-" * 65)
        print(reminder)
        print("-" * 65)

    print("\nAll reminders generated successfully.")


if __name__ == "__main__":
    main()
