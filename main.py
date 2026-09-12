"""Менеджер коротких заметок"""


def add_note(notes, text):
    notes.append(text)
    return notes


def main():
    notes = []
    add_note(notes, "Изучить git")
    add_note(notes, "Сделать первый коммит")
    for note in notes:
        print(f" - {note}")


if __name__ == "__main__":
    main()
