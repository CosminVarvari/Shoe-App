import { Component } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { User } from 'src/app/_models/user.model';
import { UserService } from 'src/app/_services/user.service';

@Component({
  selector: 'app-dialog-add-user',
  templateUrl: './dialog-add-user.component.html',
  styleUrls: ['./dialog-add-user.component.scss']
})
export class DialogAddUserComponent {
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
  })

  constructor(private userService: UserService) {}

  onSubmit() {
    let newUser = new User();
    newUser.first_name = this.userForm.value.first_name!;
    newUser.last_name = this.userForm.value.last_name!;
    newUser.email = this.userForm.value.email!;
    newUser.password = this.userForm.value.password!;
    newUser.username = this.userForm.value.username!;
    newUser.phone_number = this.userForm.value.phone_number!;
    newUser.is_manager = this.userForm.value.isManager!;
    newUser.is_employee = this.userForm.value.isEmployee!;
    newUser.is_admin = this.userForm.value.isAdmin!;
    this.userService.addUser(newUser).subscribe();
  }
}
