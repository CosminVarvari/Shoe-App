import { Component, OnDestroy, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { Router, ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { Product } from 'src/app/_models/product.model';
import { ProductService } from 'src/app/_services/product.service';
import { DialogEditProductComponent } from '../dialog-edit-product/dialog-edit-product.component';
import { DialogDeleteComponent } from '../dialog-delete/dialog-delete.component';
import { DialogAddProductComponent } from '../dialog-add-product/dialog-add-product.component';

@Component({
  selector: 'app-products-employee',
  templateUrl: './products-employee.component.html',
  styleUrls: ['./products-employee.component.scss']
})
export class ProductsEmployeeComponent implements OnInit, OnDestroy {
  products: Product[];
  currentProducts: Product[] = [];
  subscription: Subscription = new Subscription();
  product: Product;
  searchValue: string = "";
  isAvailable: boolean = false;
  panelOpenState = false;
  constructor(private productService: ProductService, private router: Router, public dialog: MatDialog)  { }
  
  ngOnInit(): void { 
    this.getAllProducts();
  }
  
  getAllProducts(): void {
    this.subscription.add(
      this.productService.getAllProducts().subscribe(data => {
        this.products = data.filter(el => el.store === 'Store A').sort((a,b) => Number(a.price) - Number(b.price));
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

  openDialogEdit(product: Product) {
    const dialogRef = this.dialog.open(DialogEditProductComponent, {
      data: product,
    });
    dialogRef.afterClosed().subscribe(result => {
      if(result == true) {
        window.location.reload();
      }
    });
  }

  openDialogDelete(product: Product) {
    const dialogRef = this.dialog.open(DialogDeleteComponent, {
      data: product.id,
    });
    dialogRef.afterClosed().subscribe(result => {
      if(result == true) {
        window.location.reload();
      }
    });
  }

  openDialogAdd() {
    const dialogRef = this.dialog.open(DialogAddProductComponent);
    dialogRef.afterClosed().subscribe(result => {
      if(result == true) {
        window.location.reload();
      }
    });
  }


  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
}
