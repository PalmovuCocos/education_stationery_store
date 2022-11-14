import { Component, OnInit } from '@angular/core';
import {SharedService} from 'src/app/shared.service';

@Component({
  selector: 'app-show-prd',
  templateUrl: './show-prd.component.html',
  styleUrls: ['./show-prd.component.css']
})
export class ShowPrdComponent implements OnInit {

  constructor(private service: SharedService) { }

  ProductList: any=[];

  ngOnInit(): void {
    this.refreshProdList();
  }

  refreshProdList(){
    this.service.getProdList().subscribe(data=>{
      this.ProductList = data;
    });
  }

}
