
def analyzesentence(sentence):
    
    total_words = len(sentence.split())

   
    all_words = sentence.split()

  
    duplicates = {}
    for word in all_words:
        if word in duplicates:
            duplicates[word] += 1
        else:
            duplicates[word] = 1


    print(f"ประโยคนั้นประกอบด้วยคำทั้งหมด {total_words} คำ")
    print(f"มีคำที่ซ้ำกัน {len(duplicates)} คำ")
    print("คำที่ซ้ำกันคือ:")
    for word, count in duplicates.items():
        print(f"- '{word}' ซ้ำกัน {count} ครั้ง")

if __name__ == "__main__":
    
    usersentence = input("กรุณาป้อนประโยคภาษาอังกฤษ: ")

    
    analyzesentence(usersentence)
