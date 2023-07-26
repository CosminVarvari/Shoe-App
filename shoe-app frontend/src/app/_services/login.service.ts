import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { User } from '../_models/user.model';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  url: string = environment.apiUrl;

  constructor(private http: HttpClient) { }

  login(username: string, password: string): Observable<User> {
    return this.http.post<User>(this.url + '/api/user/login/', {username: username, password: password});
  }

  isAuthenticated() {
    if(localStorage.getItem('currentUser') !== null && localStorage.getItem('currentUser') !== undefined)  {
      return true;
    }
    return false;
  }
}
