import { Component, Inject, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';
import { Product } from 'src/app/_models/product.model';
import { ProductService } from 'src/app/_services/product.service';

@Component({
  selector: 'app-dialog-delete',
  templateUrl: './dialog-delete.component.html',
  styleUrls: ['./dialog-delete.component.scss']
})
export class DialogDeleteComponent implements OnInit{
  id: number;

  constructor(@Inject(MAT_DIALOG_DATA) public data: number, private productService: ProductService) {}

  ngOnInit() {
    this.id = this.data;
  }

  onSubmit() {
    this.productService.deleteProduct(this.id).subscribe();
  }

}
