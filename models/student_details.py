from odoo import fields, models


class StudentDetails(models.Model):
    _name = 'student.details'
    _description = "Details of Students"

    student_name = fields.Char(string="Student Name")
    student_Roll_No = fields.Char(string="Roll No")
    student_Phone_no = fields.Integer(string="Phone No")
    student_Email = fields.Char(string="Email ID")
