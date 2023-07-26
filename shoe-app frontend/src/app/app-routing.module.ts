import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { ProductsComponent } from './components/products/products.component';
import { ProductsEmployeeComponent } from './components/products-employee/products-employee.component';
import { ProductsManagerComponent } from './components/products-manager/products-manager.component';
import { UsersComponent } from './components/users/users.component';
import {
  AuthGuardService as AuthGuard
} from './_services/auth-guard.service';
import { ManagerGuardService as ManGuard} from './_services/manager-guard.service';
import { EmployeeGuardService as EmpGuard } from './_services/employee-guard.service';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  {
    path: 'products', component: ProductsComponent, canActivate: [AuthGuard], children: [
      {
        path: 'employee',
        component: ProductsEmployeeComponent,
        canActivate: [AuthGuard],
      },
      {
        path: 'manager',
        component: ProductsManagerComponent,
        canActivate: [AuthGuard]
      }
    ]
  },
  { path: 'users', component: UsersComponent, canActivate: [AuthGuard] },
  { path: '', redirectTo: 'login', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
