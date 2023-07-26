import { Component, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { Router } from '@angular/router';
import { LoginService } from 'src/app/_services/login.service';
import { ProductService } from 'src/app/_services/product.service';
import { User } from 'src/app/_models/user.model';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  user: User;
  subscription: Subscription = new Subscription();

  username: string = "";
  password: string = "";
  show: boolean = false;

  constructor(private loginService: LoginService, private router: Router, private productService: ProductService) { }

  ngOnInit(): void { }

  login(): void {
    this.subscription.add(
      this.loginService.login(this.username, this.password).subscribe(data => {
        this.user = data;
        localStorage.setItem('currentUser', JSON.stringify(this.user));
        if(this.user.is_employee) {
          this.router.navigate(['products/employee']);
        }
        else if(this.user.is_manager) {
          this.router.navigate(['products/manager']);
        }
        else if(this.user.is_admin) {
          this.router.navigate(['users']);
        }
      })
    );
  }

  toggleShowPassword() {
    this.show = !this.show;
}
}
