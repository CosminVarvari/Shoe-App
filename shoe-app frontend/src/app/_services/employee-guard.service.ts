import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { LoginService } from './login.service';

@Injectable({
  providedIn: 'root'
})
export class EmployeeGuardService implements CanActivate {

  user: any;
  constructor(public loginService: LoginService, public router: Router) {}
  
  canActivate(): boolean {
    let ok = false;
    if(this.loginService.isAuthenticated()) {
      this.user = localStorage.getItem('currentUser');
      if(this.user.is_employee){
        this.router.navigate(['products/employee']);
        ok = true;
      }
    }
    return ok;
  }
}
