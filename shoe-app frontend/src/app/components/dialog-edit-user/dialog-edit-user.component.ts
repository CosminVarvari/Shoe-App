import { Component, Inject, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';
import { User } from 'src/app/_models/user.model';
import { UserService } from 'src/app/_services/user.service';

@Component({
  selector: 'app-dialog-edit-user',
  templateUrl: './dialog-edit-user.component.html',
  styleUrls: ['./dialog-edit-user.component.scss']
})
export class DialogEditUserComponent implements OnInit{
  userForm = new FormGroup({
    first_name: new FormControl(''),
    last_name: new FormControl(''),
    email: new FormControl(''),
    password: new FormControl(''),
    username: new FormControl(''),
    phone_number: new FormControl(''),
    isManager: new FormControl(false),
    isEmployee: new FormControl(false),
    isAdmin: new FormControl(false)
  });
  user: User;

  constructor(@Inject(MAT_DIALOG_DATA) public data: User, private userService: UserService) {}

  ngOnInit(): void {
    this.user = this.data;
    this.userForm.setValue({
      first_name: this.user.first_name, 
      last_name: this.user.last_name,
      email: this.user.email,
      password: this.user.password,
      username: this.user.username,
      phone_number: this.user.phone_number,
      isManager: this.user.is_manager,
      isEmployee: this.user.is_employee,
      isAdmin: this.user.is_admin
    });
  }

    onSubmit() {
      let newUser = new User();
      newUser.id = this.user.id;
      newUser.first_name = this.userForm.value.first_name!;
      newUser.last_name = this.userForm.value.last_name!;
      newUser.email = this.userForm.value.email!;
      newUser.password = this.userForm.value.password!;
      newUser.username = this.userForm.value.username!;
      newUser.phone_number = this.userForm.value.phone_number!;
      newUser.is_manager = this.userForm.value.isManager!;
      newUser.is_employee = this.userForm.value.isEmployee!;
      newUser.is_admin = this.userForm.value.isAdmin!;
      this.userService.updateUser(newUser).subscribe();
    }

}
