import random

words = [
    {"Hindi": "नमस्ते", "English": "Hello"},
    {"Hindi": "आप", "English": "You"},
    {"Hindi": "मैं", "English": "I"},
    {"Hindi": "क्या", "English": "What"},
    {"Hindi": "कहाँ", "English": "Where"},
    {"Hindi": "कौन", "English": "Who"},
    {"Hindi": "कब", "English": "When"},
    {"Hindi": "कैसे", "English": "How"},
    {"Hindi": "हाँ", "English": "Yes"},
    {"Hindi": "नहीं", "English": "No"},
    {"Hindi": "धन्यवाद", "English": "Thank you"},
    {"Hindi": "कृपया", "English": "Please"},
    {"Hindi": "माफ़ कीजिए", "English": "Sorry"},
    {"Hindi": "अच्छा", "English": "Good"},
    {"Hindi": "बुरा", "English": "Bad"},
    {"Hindi": "छोटा", "English": "Small"},
    {"Hindi": "बड़ा", "English": "Big"},
    {"Hindi": "खाना", "English": "Food"},
    {"Hindi": "पानी", "English": "Water"},
    {"Hindi": "मित्र", "English": "Friend"},
    {"Hindi": "परिवार", "English": "Family"},
    {"Hindi": "प्यार", "English": "Love"},
    {"Hindi": "घर", "English": "Home"},
    {"Hindi": "काम", "English": "Work"},
    {"Hindi": "पढ़ाई", "English": "Study"},
    {"Hindi": "स्कूल", "English": "School"},
    {"Hindi": "बाज़ार", "English": "Market"},
    {"Hindi": "डॉक्टर", "English": "Doctor"},
    {"Hindi": "पुस्तक", "English": "Book"},
    {"Hindi": "किताब", "English": "Book"},
    {"Hindi": "कपड़े", "English": "Clothes"},
    {"Hindi": "पैसे", "English": "Money"},
    {"Hindi": "दवाई", "English": "Medicine"},
    {"Hindi": "गाड़ी", "English": "Car"},
    {"Hindi": "बस", "English": "Bus"},
    {"Hindi": "ट्रेन", "English": "Train"},
    {"Hindi": "हवाईजहाज", "English": "Airplane"},
    {"Hindi": "खुश", "English": "Happy"},
    {"Hindi": "दुखी", "English": "Sad"},
    {"Hindi": "सुबह", "English": "Morning"},
    {"Hindi": "शाम", "English": "Evening"},
    {"Hindi": "रात", "English": "Night"},
    {"Hindi": "दिन", "English": "Day"},
    {"Hindi": "सप्ताह", "English": "Week"},
    {"Hindi": "महीना", "English": "Month"},
    {"Hindi": "साल", "English": "Year"},
    {"Hindi": "समय", "English": "Time"},
    {"Hindi": "आज", "English": "Today"},
    {"Hindi": "कल", "English": "Tomorrow/Yesterday"},
    {"Hindi": "सुंदर", "English": "Beautiful"},
    {"Hindi": "मज़ेदार", "English": "Interesting"},
    {"Hindi": "महंगा", "English": "Expensive"},
    {"Hindi": "सस्ता", "English": "Cheap"},
    {"Hindi": "खाली", "English": "Empty"},
    {"Hindi": "भरा", "English": "Full"},
    {"Hindi": "ठंडा", "English": "Cold"},
    {"Hindi": "गर्म", "English": "Hot"},
    {"Hindi": "खुशबू", "English": "Fragrance"},
    {"Hindi": "खेल", "English": "Game"},
    {"Hindi": "गीत", "English": "Song"},
    {"Hindi": "फूल", "English": "Flower"},
    {"Hindi": "पेड़", "English": "Tree"},
    {"Hindi": "पशु", "English": "Animal"},
    {"Hindi": "पक्षी", "English": "Bird"},
    {"Hindi": "मछली", "English": "Fish"},
    {"Hindi": "सड़क", "English": "Road"},
    {"Hindi": "पर्वत", "English": "Mountain"},
    {"Hindi": "नदी", "English": "River"},
    {"Hindi": "समुद्र", "English": "Ocean"},
    {"Hindi": "आकाश", "English": "Sky"},
    {"Hindi": "सूरज", "English": "Sun"},
    {"Hindi": "चाँद", "English": "Moon"},
    {"Hindi": "तारे", "English": "Stars"},
    {"Hindi": "बारिश", "English": "Rain"},
    {"Hindi": "हवा", "English": "Wind"},
    {"Hindi": "आग", "English": "Fire"},
    {"Hindi": "मिट्टी", "English": "Soil"},
    {"Hindi": "स्वस्थ", "English": "Healthy"},
    {"Hindi": "बीमार", "English": "Sick"},
    {"Hindi": "शक्ति", "English": "Power"},
    {"Hindi": "सपना", "English": "Dream"},
    {"Hindi": "सच्चाई", "English": "Truth"},
    {"Hindi": "झूठ", "English": "Lie"},
    {"Hindi": "मौसम", "English": "Weather"},
    {"Hindi": "दिशा", "English": "Direction"},
    {"Hindi": "ज्ञान", "English": "Knowledge"},
    {"Hindi": "आनंद", "English": "Joy"},
    {"Hindi": "शांति", "English": "Peace"},
    {"Hindi": "युद्ध", "English": "War"},
    {"Hindi": "उम्मीद", "English": "Hope"},
    {"Hindi": "आदमी", "English": "Man"},
    {"Hindi": "औरत", "English": "Woman"},
    {"Hindi": "बच्चा", "English": "Child"},
    {"Hindi": "भाई", "English": "Brother"},
    {"Hindi": "बहन", "English": "Sister"},
    {"Hindi": "माता", "English": "Mother"},
    {"Hindi": "पिता", "English": "Father"},
    {"Hindi": "सफाई", "English": "Cleanliness"},
    {"Hindi": "मज़ाक", "English": "Joke"}
]


def quiz_app(words):
    random.shuffle(words)

    for word in words:
        user_answer = input(f"Tell us meaning of hindi word: {word['Hindi']}: \n").strip().lower()
        correct_answer = word['English'].lower()
        if user_answer == correct_answer:
            print("You answer is correct\n")
        else:
            print("Your answer is wrong")
    

def main():
    print("Let's learn hindi by quiz")
    print("Press enter to start quiz")
    quiz_app(words)

main()