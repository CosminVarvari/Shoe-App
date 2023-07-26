import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { TranslateService } from '@ngx-translate/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit{  
  panelOpenState = false;
  constructor(private translateService: TranslateService,private router: Router){ }

  ngOnInit(): void {
  }

  logout() {
    localStorage.clear();
    this.router.navigate(['login']);
  }
  selectLanguage(language: string) {
    this.translateService.use(language);
  }
}
