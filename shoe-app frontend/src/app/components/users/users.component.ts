import { Component, OnDestroy, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { User } from 'src/app/_models/user.model';
import { UserService } from 'src/app/_services/user.service';
import { DialogAddUserComponent } from '../dialog-add-user/dialog-add-user.component';
import { DialogDeleteUserComponent } from '../dialog-delete-user/dialog-delete-user.component';
import { DialogEditUserComponent } from '../dialog-edit-user/dialog-edit-user.component';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.scss']
})
export class UsersComponent implements OnInit, OnDestroy {
  users: User[];
  currentUsers: User[] = [];
  subscription: Subscription = new Subscription();
  user: User;
  isEmployee: boolean;
  isManager: boolean;
  panelOpenState = false;
  constructor(private userService: UserService, private router: Router, public dialog: MatDialog) { }

  ngOnInit(): void {
    this.getAllUsers();
  }

  getAllUsers(): void {
    this.subscription.add(
      this.userService.getAllUsers().subscribe(data => {
        this.users = data.filter(el => el.is_admin === false).filter(el => el.id !== 1);
        console.log(this.users);
        this.currentUsers = this.users;
        console.log(this.currentUsers);
      })
    );
  }

  filterEmployees() {
    if (this.isEmployee === true) {
      this.currentUsers = this.getEmployeeUsers();
      this.isManager = false;
    }
    else {
      this.currentUsers = this.users;
    }
  }

  filterManagers() {
    if (this.isManager === true) {
      this.currentUsers = this.getManagerUsers();
      this.isEmployee = false;
    }
    else {
      this.currentUsers = this.users;
    }
  }

  getEmployeeUsers(): User[] {
    return this.users.filter(el => el.is_employee === true);
  }

  getManagerUsers(): User[] {
    return this.users.filter(el => el.is_manager === true);
  }

  openDialogEdit(user: User) {
    const dialogRef = this.dialog.open(DialogEditUserComponent, {
      data: user,
    });
    dialogRef.afterClosed().subscribe(result => {
      if (result == true) {
        window.location.reload();
      }
    });
  }

  openDialogDelete(user: User) {
    const dialogRef = this.dialog.open(DialogDeleteUserComponent, {
      data: user.id,
    });
    dialogRef.afterClosed().subscribe(result => {
      if (result == true) {
        window.location.reload();
      }
    });
  }

  openDialogAdd() {
    const dialogRef = this.dialog.open(DialogAddUserComponent);
    dialogRef.afterClosed().subscribe(result => {
      if (result == true) {
        window.location.reload();
      }
    });
  }


  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
}
