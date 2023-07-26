import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Product } from '../_models/product.model';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  url: string = environment.apiUrl;
  constructor(private http: HttpClient) { }

  getAllProducts(): Observable<Product[]> {
    return this.http.get<Product[]>(this.url + '/api/products/');
  }

  getProductById(id: number): Observable<Product> {
    return this.http.get<Product>(this.url + `/api/products/detail/${id}/`);
  }

  addProduct(product: Product): Observable<Product> {
    return this.http.post<Product>(this.url + '/api/products/add/', product);
  }

  deleteProduct(id: number): Observable<unknown> {
    return this.http.delete(this.url + `/api/products/delete/${id}/`);
  }
  
  updateProduct(product: Product): Observable<Product> {
    return this.http.put<Product>(this.url + '/api/products/update/', product);
  }
}
