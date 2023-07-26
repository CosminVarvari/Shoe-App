import { UserService } from 'src/app/_services/user.service';
import { Component, Inject, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';
@Component({
  selector: 'app-dialog-delete-user',
  templateUrl: './dialog-delete-user.component.html',
  styleUrls: ['./dialog-delete-user.component.scss']
})
export class DialogDeleteUserComponent implements OnInit{
  id: number;

  constructor(@Inject(MAT_DIALOG_DATA) public data: number, private userService: UserService) {}

  ngOnInit() {
    this.id = this.data;
  }

  onSubmit() {
    this.userService.deleteUser(this.id).subscribe();
  }
}
