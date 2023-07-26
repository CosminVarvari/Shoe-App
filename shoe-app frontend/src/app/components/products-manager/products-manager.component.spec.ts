import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProductsManagerComponent } from './products-manager.component';

describe('ProductsManagerComponent', () => {
  let component: ProductsManagerComponent;
  let fixture: ComponentFixture<ProductsManagerComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ProductsManagerComponent]
    });
    fixture = TestBed.createComponent(ProductsManagerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
