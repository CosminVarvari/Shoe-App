import { Component, OnDestroy, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { Product } from 'src/app/_models/product.model';
import { ProductService } from 'src/app/_services/product.service';

@Component({
  selector: 'app-products-manager',
  templateUrl: './products-manager.component.html',
  styleUrls: ['./products-manager.component.scss']
})
export class ProductsManagerComponent implements OnInit,  OnDestroy{
  products: Product[];
  currentProducts: Product[] = [];
  subscription: Subscription = new Subscription();
  product: Product;
  searchValue: string = "";
  isAvailable: boolean = false;
  panelOpenState = false;
  constructor(private productService: ProductService)  { }
  
  ngOnInit(): void { 
    this.getAllProducts();
  }
  
  getAllProducts(): void {
    this.subscription.add(
      this.productService.getAllProducts().subscribe(data => {
        this.products = data.sort((a,b) => {
          if(a.store > b.store) {
            return 1;
          }
          else if(a.store < b.store) {
            return -1;
          }
          return 0;
        } );
        this.currentProducts = this.products;
      })
    )
  }

  filterProducts() {
    if(this.isAvailable === true) {
      this.currentProducts = this.getAvailableProducts();
    }
    else {
      this.currentProducts = this.products;
    }
  }

  getAvailableProducts():Product[] {
    return this.products.filter(el => el.is_available === true);
  }

  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
}
