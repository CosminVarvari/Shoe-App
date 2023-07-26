import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { User } from '../_models/user.model';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  url: string = environment.apiUrl;
  constructor(private http: HttpClient) { }

  getAllUsers(): Observable<User[]> {
    return this.http.get<User[]>(this.url + '/api/user/');
  }

  getUserById(id: number): Observable<User> {
    return this.http.get<User>(this.url + `/api/user/detail/${id}`);
  }

  addUser(user: User): Observable<User> {
    return this.http.post<User>(this.url + '/api/user/add/', user);
  }

  deleteUser(id: number): Observable<unknown> {
    return this.http.delete(this.url + `/api/user/delete/${id}/`);
  }
  
  updateUser(user: User): Observable<User> {
    return this.http.put<User>(this.url + '/api/user/update/', user);
  }
}
