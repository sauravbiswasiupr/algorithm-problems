# Design an employee feedback system
#
# 1. Employee --> Intern, Normal, Product Manager, H.R, Director, CEO
# 2. Question --> Specific employee gets specific set of questions catered to his needs.
# 3. Answer --> Associated with a question (for sake of brevity we use the numbers 1 to 5)
# 4. FeedbackForm --> Contains a set of (question, answer) tuples, targeted towards a specific kind of employee
# 5. FeedbackManager --> Central hub which disseminated feedback forms to users, collects the feedbacks
# and persists them in a data store.


class Question:
    def __init__(self, text):
      self.text = text
      self.answer = None
      self.extra_information = None
      self.answered = False

    def change_text(self, new_text):
       self.text = new_text

    def get_text(self):
       return self.text

    def set_answer(self, ans):
       self.answer = ans

    def get_answer(self):
       return self.answer

    def submit_answer(self, ans):
       if not self.answered:
          self.set_answer(ans)
          self.answered = True

    def answered(self):
       return self.answered

    def set_extra_information(self, data):
       self.extra_information = data

    def get_extra_information(self):
        return self.extra_information


class FeedbackForm:
    def __init__(self, idx, questions):
       self.id = idx
       self.questions = [Question(q) for q in questions]
       self.submitted = False
       self.questions_answered_till_now = 0

    def submitted(self):
       return self.submitted

    def save_and_submit(self):
        if self.questions_answered_till_now < len(self.questions):
            print "Please complete the feedback"
            return
        self.submitted = True

    def submit_feedback_for_question(self, question_num, answer):
       self.questions[question_num].submit_answer(answer)
       self.questions_answered_till_now += 1


class Employee:
    def __init__(self, name, idx, designation):
       self.name = name
       self.id = idx
       self.designation = designation
       self.feedback_forms = {}

    def send_feedback_form_to_employee(self, form):
       if form.id not in self.feedback_forms:
          self.feedback_forms[form.id] = form

    def complete_form(self, form_id):
        form = self.feedback_forms.get(form_id)
        if not form:
            print "Employee {} didn't receive this form with id: {}".format(self.id, form_id)
            return

        if not form.submitted:
          for id in range(len(form.questions)):
             ans = raw_input()
             form.submit_feedback_for_question(id, ans)


        form.save_and_submit()


class Intern(Employee):
   def __init__(self, name, id, designation):
      super(Intern, self).__init__(name, id, designation)


class ProductManager(Employee):
   def __init__(self, *args, **kwargs):
      super(ProductManager, self).__init__(*args, **kwargs)
      self.people_managed = {}
      self.forms_created = {}

   def add_people_to_team(self, id, name, designation):
      if id not in self.people_managed:
         self.people_managed[id] = Employee(name, id, designation)

   def send_form_to_specific_employee(self, id, form):
       if id not in self.people_managed:
          self.delegate_to_upper_management()
       else:
          employee = self.people_managed[id]
          employee.send_feedback_form_to_employee(form)

   def get_or_create_form(self, form_id, questions):
      if form_id not in self.forms_created:
          form = FeedbackForm(form_id, questions)
          self.forms_created[form_id] = form
      else:
          form = self.forms_created[form_id]
      return form
