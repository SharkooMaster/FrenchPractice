from tkinter import *
import random
import json

class eva:
	def __init__(self):
		self.root = Tk()
		self.root.config(background="#f7b24a")

		self.verbs = self.get_verbs()
		self.verbs_len = len(self.verbs)
		self.index = 0
		self.HowFar = 0

		self.root.title = "Eva's Verb Anxiety" # E V A
		self.root.minsize(width=800, height=600)
		
		self.set_ui()
	
	def run(self):
		self.root.mainloop()
	
	def new_rand(self):
		self.index = random.randint(0, self.verbs_len - 1)
	
	def set_ui(self):
		self.frame = Frame(self.root)
		self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

		self.inner_frame = Frame(self.frame)
		self.inner_frame.pack()

		self.title_label = Label(self.inner_frame, text="Eva's Verb Anxiety", font=("Helvetica", 24))
		self.title_label.config(foreground="#912121")

		self.track_label = Label(self.inner_frame, text="", font=("Helvetica", 14))
		self.french_label = Label(self.inner_frame, text="Click next to start", font=("Helvetica", 24))
		self.input_box = Entry(self.inner_frame, width=30, font=("Helvetica", 18))
		self.check_btn = Button(self.inner_frame, text="Check Answer", command=self.check_verb)
		self.next_btn = Button(self.inner_frame, text="Next Verb", command=self.next_verb)
		self.show_btn = Button(self.inner_frame, text="Show Correct Verb", command=self.show_verb)
		self.result_label = Label(self.inner_frame, text="", font=("Helvetica", 14))

		self.title_label.pack(pady=5)
		self.track_label.pack(pady=5)
		self.french_label.pack(pady=10)
		self.input_box.pack(pady=10, padx=20)
		self.next_btn.pack(pady=10)
		#self.check_btn.pack(pady=10)
		self.show_btn.pack(pady=10)
		self.result_label.pack(pady=10)
	
	def get_verbs(self):
		with open("./group_a.json", "r") as f:
			to_ret = json.loads(f.read())["verbs"]
		return to_ret
	
	def show_verb(self):
		self.result_label.config(text=self.verbs[self.index]["e"])

	def check_verb(self, ret = False):
		_answer = self.input_box.get(1.0, END).strip()
		expected = self.verbs[self.index]["e"]
		if(_answer == expected):
			self.result_label.config(text="Nicely done Jimbeaux!")
		else:
			self.result_label.config(text="Do better Jimothy!")
		if(ret): return (_answer == expected)

	def next_verb(self):
		res = self.check_verb(True)

		if(res or self.HowFar == 0):
			self.HowFar += 1
			self.new_rand()
			self.french_label.config(text=self.verbs[self.index]["f"])
			self.track_label.config(text=f"How many I've done: {self.HowFar - 1}")
			self.result_label.config(text="")
			self.input_box.delete("1.0", END)

main = eva()
main.run()