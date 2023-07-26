import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { LoginService } from './login.service';

@Injectable({
  providedIn: 'root'
})
export class ManagerGuardService implements CanActivate{

  user: any;
  constructor(public loginService: LoginService, public router: Router) {}
  
  canActivate(): boolean {
    let ok = false;
    if(this.loginService.isAuthenticated()) {
      this.user = localStorage.getItem('currentUser');
      if(this.user.is_manager){
        this.router.navigate(['products/manager']);
        ok = true;
      }
    }
    return ok;
  }
}
