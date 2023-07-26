import { Component, Inject, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';
import { Product } from 'src/app/_models/product.model';
import { ProductService } from 'src/app/_services/product.service';

@Component({
  selector: 'app-dialog-edit-product',
  templateUrl: './dialog-edit-product.component.html',
  styleUrls: ['./dialog-edit-product.component.scss']
})
export class DialogEditProductComponent implements OnInit {
  productForm = new FormGroup({
    name: new FormControl(''),
    price: new FormControl(''),
    description: new FormControl(''),
    store: new FormControl(''),
    producer: new FormControl(''),
    isAvailable: new FormControl(false)
  });
  product: Product;
  
  constructor(@Inject(MAT_DIALOG_DATA) public data: Product, private productService: ProductService) {}

  ngOnInit(): void {
    this.product = this.data;
    this.productForm.setValue({
      name: this.product.name, 
      price: this.product.price,
      description: this.product.description,
      store: this.product.store,
      producer: this.product.producer,
      isAvailable: this.product.is_available
    });
  }

  onSubmit() {
    let newProduct = new Product();
    newProduct.id = this.product.id;
    newProduct.name = this.productForm.value.name!;
    newProduct.price = this.productForm.value.price!;
    newProduct.description = this.productForm.value.description!;
    newProduct.store = this.productForm.value.store!;
    newProduct.producer = this.productForm.value.producer!;
    newProduct.is_available = this.productForm.value.isAvailable!;
    this.productService.updateProduct(newProduct).subscribe();
  }

}
