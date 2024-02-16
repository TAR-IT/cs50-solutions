from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        # Add the header to the top of each page
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "CS50 Shirtificate", 0, 1, "C")

    def create_shirtificate(self, name):
        self.add_page()
        self.set_auto_page_break(auto=True, margin=15)
        self.set_font("Arial", "B", 20)

        # Center the shirt image horizontally
        self.image("shirtificate.png", x=50, w=110)

        # Add the user's name on top of the shirt (centered horizontally)
        self.set_text_color(255, 255, 255)  # White color for the text
        self.cell(0, -50, name, 0, 1, "C")

if __name__ == "__main__":
    name = input("Enter your name: ")

    pdf = Shirtificate(orientation="P", unit="mm", format="A4")
    pdf.create_shirtificate(name)
    pdf.output("shirtificate.pdf")
