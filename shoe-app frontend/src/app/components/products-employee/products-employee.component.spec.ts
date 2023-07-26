import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProductsEmployeeComponent } from './products-employee.component';

describe('ProductsEmployeeComponent', () => {
  let component: ProductsEmployeeComponent;
  let fixture: ComponentFixture<ProductsEmployeeComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ProductsEmployeeComponent]
    });
    fixture = TestBed.createComponent(ProductsEmployeeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
