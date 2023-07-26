import { Component, Inject, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';
import { Product } from 'src/app/_models/product.model';
import { ProductService } from 'src/app/_services/product.service';

@Component({
  selector: 'app-dialog-add-product',
  templateUrl: './dialog-add-product.component.html',
  styleUrls: ['./dialog-add-product.component.scss']
})
export class DialogAddProductComponent {
  productForm = new FormGroup({
    name: new FormControl(''),
    price: new FormControl(''),
    description: new FormControl(''),
    store: new FormControl(''),
    producer: new FormControl(''),
    isAvailable: new FormControl(false)
  });
  
  constructor(private productService: ProductService) {}


  onSubmit() {
    let newProduct = new Product();
    newProduct.name = this.productForm.value.name!;
    newProduct.price = this.productForm.value.price!;
    newProduct.description = this.productForm.value.description!;
    newProduct.store = this.productForm.value.store!;
    newProduct.producer = this.productForm.value.producer!;
    newProduct.is_available = this.productForm.value.isAvailable!;
    this.productService.addProduct(newProduct).subscribe();
  }
}
